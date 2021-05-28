"""
pyPreservica ContentAPI module definition

A client library for the Preservica Repository web services Content API
https://us.preservica.com/api/content/documentation.html

author:     James Carr
licence:    Apache License 2.0

"""

import csv

from pyPreservica.common import *

logger = logging.getLogger(__name__)


class ContentAPI(AuthenticatedAPI):

    def __init__(self, username=None, password=None, tenant=None, server=None, use_shared_secret=False):
        super().__init__(username, password, tenant, server, use_shared_secret)
        self.callback = None

    class SearchResult:
        def __init__(self, metadata, refs, hits, results_list, next_start):
            self.metadata = metadata
            self.refs = refs
            self.hits = int(hits)
            self.results_list = results_list
            self.next_start = next_start

    def search_callback(self, fn):
        self.callback = fn

    def object_details(self, entity_type, reference):
        headers = {HEADER_TOKEN: self.token, 'Content-Type': 'application/json'}
        params = {'id': f'sdb:{entity_type.value}|{reference}'}
        request = self.session.get(f'https://{self.server}/api/content/object-details', params=params, headers=headers)
        if request.status_code == requests.codes.ok:
            return request.json()["value"]
        elif request.status_code == requests.codes.not_found:
            logger.error(f"The requested reference is not found in the repository: {reference}")
            raise RuntimeError(reference, "The requested reference is not found in the repository")
        elif request.status_code == requests.codes.unauthorized:
            self.token = self.__token__()
            return self.object_details(entity_type, reference)
        else:
            logger.error(f"object_details failed with error code: {request.status_code}")
            raise RuntimeError(request.status_code, f"object_details failed with error code: {request.status_code}")

    def download(self, reference, filename):
        headers = {HEADER_TOKEN: self.token, 'Content-Type': 'application/octet-stream'}
        params = {'id': f'sdb:IO|{reference}'}
        with self.session.get(f'https://{self.server}/api/content/download', params=params, headers=headers,
                              stream=True) as req:
            if req.status_code == requests.codes.ok:
                with open(filename, 'wb') as file:
                    for chunk in req.iter_content(chunk_size=CHUNK_SIZE):
                        file.write(chunk)
                        file.flush()
                file.close()
                return filename
            elif req.status_code == requests.codes.unauthorized:
                self.token = self.__token__()
                return self.download(reference, filename)
            elif req.status_code == requests.codes.not_found:
                logger.error(f"The requested asset reference is not found in the repository: {reference}")
                raise RuntimeError(reference, "The requested reference is not found in the repository")
            else:
                logger.error(f"download failed with error code: {req.status_code}")
                raise RuntimeError(req.status_code, f"download failed with error code: {req.status_code}")

    def thumbnail(self, entity_type, reference, filename, size=Thumbnail.LARGE):
        headers = {HEADER_TOKEN: self.token, 'accept': 'image/png'}
        params = {'id': f'sdb:{entity_type}|{reference}', 'size': f'{size.value}'}
        with self.session.get(f'https://{self.server}/api/content/thumbnail', params=params, headers=headers,
                              stream=True) as req:
            if req.status_code == requests.codes.ok:
                with open(filename, 'wb') as file:
                    for chunk in req.iter_content(chunk_size=CHUNK_SIZE):
                        file.write(chunk)
                        file.flush()
                return filename
            elif req.status_code == requests.codes.unauthorized:
                self.token = self.__token__()
                return self.thumbnail(entity_type, reference, filename, size)
            elif req.status_code == requests.codes.not_found:
                logger.error(req.content.decode("utf-8"))
                logger.error(f"The requested reference is not found in the repository: {reference}")
                raise RuntimeError(reference, "The requested reference is not found in the repository")
            else:
                logger.error(f"thumbnail failed with error code: {req.status_code}")
                raise RuntimeError(req.status_code, f"thumbnail failed with error code: {req.status_code}")

    def indexed_fields(self):
        headers = {HEADER_TOKEN: self.token}
        results = self.session.get(f'https://{self.server}/api/content/indexed-fields', headers=headers)
        if results.status_code == requests.codes.ok:
            fields = list()
            for ob in results.json()["value"]:
                field = f'{ob["shortName"]}.{ob["index"]}'
                fields.append(field)
            return fields
        elif results.status_code == requests.codes.unauthorized:
            self.token = self.__token__()
            return self.indexed_fields()
        else:
            logger.error(f"indexed_fields failed with error code: {results.status_code}")
            raise RuntimeError(results.status_code, f"indexed_fields failed with error code: {results.status_code}")

    def simple_search_csv(self, query: str = "%", csv_file="search.csv", *args):
        page_size = 50
        if len(args) == 0:
            metadata_fields = ["xip.reference", "xip.title", "xip.description", "xip.document_type",
                               "xip.parent_ref", "xip.security_descriptor"]
        else:
            metadata_fields = list(*args)
        if "xip.reference" not in metadata_fields:
            metadata_fields.insert(0, "xip.reference")
        with open(csv_file, newline='', mode="wt", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=metadata_fields)
            writer.writeheader()
            writer.writerows(self.simple_search_list(query, page_size, *args))

    def simple_search_list(self, query: str = "%", *args):
        page_size = 50
        search_result = self._simple_search(query, 0, page_size, *args)
        for e in search_result.results_list:
            yield e
        found = len(search_result.results_list)
        while search_result.hits > found:
            search_result = self._simple_search(query, found, page_size, *args)
            for e in search_result.results_list:
                yield e
            found = found + len(search_result.results_list)

    def _simple_search(self, query: str = "%", start_index: int = 0, page_size: int = 10, *args):
        start_from = str(start_index)
        headers = {'Content-Type': 'application/x-www-form-urlencoded', HEADER_TOKEN: self.token}
        query_term = ('{ "q":  "%s" }' % query)
        if len(args) == 0:
            metadata_fields = "xip.title,xip.description,xip.document_type,xip.parent_ref,xip.security_descriptor"
        else:
            metadata_fields = ','.join(*args)
        payload = {'start': start_from, 'max': str(page_size), 'metadata': metadata_fields, 'q': query_term}
        results = self.session.post(f'https://{self.server}/api/content/search', data=payload, headers=headers)
        results_list = list()
        if results.status_code == requests.codes.ok:
            json = results.json()
            metadata = json['value']['metadata']
            refs = list(json['value']['objectIds'])
            refs = list(map(lambda x: content_api_identifier_to_type(x), refs))
            hits = int(json['value']['totalHits'])

            for m_row, r_row in zip(metadata, refs):
                results_map = dict()
                results_map['xip.reference'] = r_row[1]
                for li in m_row:
                    results_map[li['name']] = li['value']
                results_list.append(results_map)
            next_start = start_index + page_size

            if self.callback is not None:
                value = str(f'{len(results_list) + start_index}:{hits}')
                self.callback(value)

            search_results = self.SearchResult(metadata, refs, hits, results_list, next_start)
            return search_results
        elif results.status_code == requests.codes.unauthorized:
            self.token = self.__token__()
            return self._simple_search(query, start_index, page_size, *args)
        else:
            logger.error(f"search failed with error code: {results.status_code}")
            raise RuntimeError(results.status_code, f"simple_search failed with error code: {results.status_code}")

    def search_index_filter_csv(self, query: str = "%", csv_file="search.csv", filter_values: dict = None):
        page_size = 50
        if filter_values is None:
            filter_values = dict()
        if "xip.reference" not in filter_values:
            filter_values["xip.reference"] = ""

        header_fields = list(filter_values.keys())
        index = header_fields.index("xip.reference")
        header_fields.insert(0, header_fields.pop(index))
        with open(csv_file, newline='', mode="wt", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header_fields)
            writer.writeheader()
            writer.writerows(self.search_index_filter_list(query, page_size, filter_values))

    def search_index_filter_list(self, query: str = "%", page_size: int = 25, filter_values: dict = None):
        search_result = self._search_index_filter(query, 0, page_size, filter_values)
        for e in search_result.results_list:
            yield e
        found = len(search_result.results_list)
        while search_result.hits > found:
            search_result = self._search_index_filter(query, found, page_size, filter_values)
            for e in search_result.results_list:
                yield e
            found = found + len(search_result.results_list)

    def _search_index_filter(self, query: str = "%", start_index: int = 0, page_size: int = 25,
                             filter_values: dict = None):
        start_from = str(start_index)
        headers = {'Content-Type': 'application/x-www-form-urlencoded', HEADER_TOKEN: self.token}

        field_list = list()
        for key, value in filter_values.items():
            if value == "":
                field_list.append('{' f' "name": "{key}", "values": [] ' + '}')
            else:
                field_list.append('{' f' "name": "{key}", "values": ["{value}"] ' + '}')

        filter_terms = ','.join(field_list)

        query_term = ('{ "q":  "%s",  "fields":  [ %s ] }' % (query, filter_terms))

        payload = {'start': start_from, 'max': str(page_size), 'metadata': list(filter_values.keys()), 'q': query_term}
        results = self.session.post(f'https://{self.server}/api/content/search', data=payload, headers=headers)
        results_list = list()
        if results.status_code == requests.codes.ok:
            json = results.json()
            metadata = json['value']['metadata']
            refs = list(json['value']['objectIds'])
            refs = list(map(lambda x: content_api_identifier_to_type(x), refs))
            hits = int(json['value']['totalHits'])

            for m_row, r_row in zip(metadata, refs):
                results_map = dict()
                results_map['xip.reference'] = r_row[1]
                for li in m_row:
                    results_map[li['name']] = li['value']
                results_list.append(results_map)
            next_start = start_index + page_size

            if self.callback is not None:
                value = str(f'{len(results_list) + start_index}:{hits}')
                self.callback(value)

            search_results = self.SearchResult(metadata, refs, hits, results_list, next_start)
            return search_results
        elif results.status_code == requests.codes.unauthorized:
            self.token = self.__token__()
            return self._search_index_filter(query, start_index, page_size, filter_values)
        else:
            logger.error(f"search failed with error code: {results.status_code}")
            raise RuntimeError(results.status_code, f"search_index_filter failed")

    class ReportProgressCallBack:
        def __init__(self):
            self.current = 0
            self.total = 0
            self._lock = threading.Lock()

        def __call__(self, value):
            with self._lock:
                values = value.split(":")
                self.total = int(values[1])
                self.current = int(values[0])
                percentage = (self.current / self.total) * 100
                sys.stdout.write("\rProcessing Hits %s from %s  (%.2f%%)" % (self.current, self.total, percentage))
                sys.stdout.flush()

    def __report_security_tag_frequency(self, report_name="security_report.svg"):
        import pygal
        from pygal.style import BlueStyle
        results = {}
        self.search_callback(self.ReportProgressCallBack())
        filters = {"xip.security_descriptor": "*", "xip.document_type": "IO", "xip.parent_ref": "*"}
        for hit in self.search_index_filter_list(query="%", page_size=50, filter_values=filters):
            tag = hit['xip.security_descriptor'][0]
            ref = hit['xip.reference']
            if tag in results:
                results[tag] = results[tag] + 1
            else:
                results[tag] = 1

        bar_chart = pygal.HorizontalBar(show_legend=False)
        bar_chart.title = "Security Tag Frequency"
        bar_chart.style = BlueStyle
        bar_chart.x_title = 'Number of Assets'
        bar_chart.x_labels = results.keys()
        bar_chart.add("Security Tag", results)

        bar_chart.render_to_file(report_name)

        sys.stdout.write("\nReport Completed. Open file " + report_name + " in your browser")
        sys.stdout.flush()
