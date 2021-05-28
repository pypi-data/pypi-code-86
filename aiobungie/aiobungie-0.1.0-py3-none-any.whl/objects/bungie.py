'''
MIT License

Copyright (c) 2020 - Present nxtlo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
from typing import Optional, Any, Dict, List, Sequence

class Careers(object):
    __slots__: Sequence[str] = ("response",)
    
    def __init__(self, data) -> None:
        self.response: Optional[Dict[str, Any]] = data.get("Response")
        self.response = self.response.get('categories')

    @property
    def categories(self) -> List[Any]:
        for i in self.response:
            return i

class News(object):
    __slots__: Sequence[str] = ('response',)

    def __init__(self, data: Dict[str, Any]) -> None:
        self.response: Optional[Dict[str, Any]] = data.get('response')

    @property
    def _(self) -> None:
        pass


class DestinyContent(object):
    __slots__ = ('response')

    def __init__(self, data: Optional[Dict[Any, Any]]) -> None:
        self.response: Dict[str, Any] = data.get('response')

    @property
    def _(self) -> None:
        pass
