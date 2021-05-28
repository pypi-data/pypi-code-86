"""
    test_dQuery
    ~~~~~~~~~~~~~~~
    unit tests for domonic.dQuery

"""

import time
import unittest
# import requests
# from mock import patch
# from domonic.javascript import Math

from domonic.dom import *
from domonic.html import *
from domonic.dQuery import *


class domonicTestCase(unittest.TestCase):

    # domonic.dQuery.º
    def test_dQuery_hello(self):
        d = html(head(body(li(_class='things'), div(_id="test"))))
        º(d)
        print( '---** -' )
        print( º('#test') )
        print( '---** -' )
        print( º('.things') )
        print( '---** -' )

        print( 'a::' )
        a = º('<div class="test2"></div>')
        print( a )

        print( 'b::' )
        b = º('#test').append(a)
        print(b)

        print(d)

        pass

    def test_dQuery_add(self):
        pass

    def test_dQuery_addBack(self):
        pass

    def test_dQuery_addClass(self):
        pass

    def test_dQuery_after(self):
        pass

    def test_dQuery_ajaxComplete(self):
        pass

    def test_dQuery_ajaxError(self):
        pass

    def test_dQuery_ajaxSend(self):
        pass

    def test_dQuery_ajaxStart(self):
        pass

    def test_dQuery_ajaxStop(self):
        pass

    def test_dQuery_ajaxSuccess(self):
        pass

    def test_dQuery_andSelf(self):
        pass

    def test_dQuery_animate(self):
        pass

    def test_dQuery_append(self):
        print("TEST APPEND")
        # doc = html()
        # º(doc)
        # doc.append("some text")
        # print(doc.html())
        # d = º('<div></div>').append("some text")
        # self.assertEqual(str(d), '<div>some text</div>')
        pass

    def test_dQuery_appendTo(self):
        pass

    def test_dQuery_attr(self):
        pass

    def test_dQuery_before(self):
        pass

    def test_dQuery_bind(self):
        pass

    def test_dQuery_blur(self):
        pass

    def test_dQuery_change(self):
        pass

    def test_dQuery_children(self):
        pass

    def test_dQuery_clearQueue(self):
        pass

    def test_dQuery_click(self):
        pass

    def test_dQuery_clone(self):
        pass

    def test_dQuery_closest(self):
        pass

    def test_dQuery_contents(self):
        pass

    def test_dQuery_context(self):
        pass

    def test_dQuery_contextmenu(self):
        pass

    def test_dQuery_css(self):
        pass

    def test_dQuery_data(self):
        pass

    def test_dQuery_dblclick(self):
        pass

    def test_dQuery_delay(self):
        pass

    def test_dQuery_delegate(self):
        pass

    def test_dQuery_dequeue(self):
        pass

    def test_dQuery_detach(self):
        pass

    def test_dQuery_die(self):
        pass

    def test_dQuery_each(self):
        pass

    def test_dQuery_empty(self):
        pass

    def test_dQuery_end(self):
        pass

    def test_dQuery_eq(self):
        pass

    def test_dQuery_error(self):
        pass

    def test_dQuery_even(self):
        pass

    def test_dQuery_fadeIn(self):
        pass

    def test_dQuery_fadeOut(self):
        pass

    def test_dQuery_fadeTo(self):
        pass

    def test_dQuery_fadeToggle(self):
        pass

    def test_dQuery_filter(self):
        pass

    def test_dQuery_find(self):
        pass

    def test_dQuery_finish(self):
        pass

    def test_dQuery_first(self):
        pass

    def test_dQuery_focus(self):
        pass

    def test_dQuery_focusin(self):
        pass

    def test_dQuery_focusout(self):
        pass

    def test_dQuery_get(self):
        pass

    def test_dQuery_has(self):
        pass

    def test_dQuery_hasClass(self):
        pass

    def test_dQuery_height(self):
        pass

    def test_dQuery_hide(self):
        pass

    def test_dQuery_hover(self):
        pass

    def test_dQuery_html(self):
        pass

    def test_dQuery_index(self):
        pass

    def test_dQuery_innerHeight(self):
        pass

    def test_dQuery_innerWidth(self):
        pass

    def test_dQuery_insertAfter(self):
        pass

    def test_dQuery_insertBefore(self):
        pass

    # def test_dQuery_is(self):
        # pass

    def test_dQuery_keydown(self):
        pass

    def test_dQuery_keypress(self):
        pass

    def test_dQuery_keyup(self):
        pass

    def test_dQuery_last(self):
        pass

    def test_dQuery_length(self):
        pass

    def test_dQuery_live(self):
        pass

    def test_dQuery_load(self):
        pass

    def test_dQuery_map(self):
        pass

    def test_dQuery_mousedown(self):
        pass

    def test_dQuery_mouseenter(self):
        pass

    def test_dQuery_mouseleave(self):
        pass

    def test_dQuery_mousemove(self):
        pass

    def test_dQuery_mouseout(self):
        pass

    def test_dQuery_mouseover(self):
        pass

    def test_dQuery_mouseup(self):
        pass

    def test_dQuery_next(self):
        pass

    def test_dQuery_nextAll(self):
        pass

    def test_dQuery_nextUntil(self):
        pass

    # def test_dQuery_not(self):
        # pass

    def test_dQuery_odd(self):
        pass

    def off(self, event):
        pass

    def test_dQuery_offset(self):
        pass

    def test_dQuery_offsetParent(self):
        pass

    def on(self, event, callback):
        pass

    def test_dQuery_one(self):
        pass

    def test_dQuery_outerHeight(self):
        pass

    def test_dQuery_outerWidth(self):
        pass

    def test_dQuery_parent(self):
        pass

    def test_dQuery_parents(self):
        pass

    def test_dQuery_parentsUntil(self):
        pass

    def test_dQuery_position(self):
        pass

    def prepend(self, html):
        pass

    def test_dQuery_prependTo(self):
        pass

    def test_dQuery_prev(self):
        pass

    def test_dQuery_prevAll(self):
        pass

    def test_dQuery_prevUntil(self):
        pass

    def test_dQuery_promise(self):
        pass

    def test_dQuery_prop(self):
        pass

    def test_dQuery_pushStack(self):
        pass

    def test_dQuery_queue(self):
        pass

    def test_dQuery_ready(self):
        pass

    def test_dQuery_remove(self):
        pass

    def test_dQuery_removeAttr(self):
        pass

    def test_dQuery_removeClass(self):
        pass

    def test_dQuery_removeData(self):
        pass

    def test_dQuery_removeProp(self):
        pass

    def test_dQuery_replaceAll(self):
        pass

    def test_dQuery_replaceWith(self):
        pass

    def test_dQuery_resize(self):
        pass

    def test_dQuery_scroll(self):
        pass

    def test_dQuery_scrollLeft(self):
        pass

    def test_dQuery_scrollTop(self):
        pass

    def test_dQuery_select(self):
        pass

    def test_dQuery_serialize(self):
        pass

    def test_dQuery_serializeArray(self):
        pass

    def test_dQuery_show(self):
        pass

    def test_dQuery_siblings(self):
        pass

    def test_dQuery_size(self):
        pass

    def test_dQuery_slice(self):
        pass

    def test_dQuery_slideDown(self):
        pass

    def test_dQuery_slideToggle(self):
        pass

    def test_dQuery_slideUp(self):
        pass

    def test_dQuery_stop(self):
        pass

    def test_dQuery_submit(self):
        pass

    def test_dQuery_text(self):
        pass

    def test_dQuery_toArray(self):
        pass

    def test_dQuery_toggle(self):
        pass

    def test_dQuery_toggleClass(self):
        pass

    def test_dQuery_trigger(self):
        pass

    def test_dQuery_triggerHandler(self):
        pass

    def test_dQuery_unbind(self):
        pass

    def test_dQuery_undelegate(self):
        pass

    def test_dQuery_unload(self):
        pass

    def test_dQuery_unwrap(self):
        pass

    def val(self, newVal=None):
        pass

    def test_dQuery_width(self):
        pass

    def test_dQuery_wrap(self):
        pass

    def test_dQuery_wrapAll(self):
        pass

    def test_dQuery_wrapInner(self):
        pass

    def test_dQuery_staticmethods(self):
        print("test_dQuery_staticmethods::::::::::::::::::")

        d = html()
        º(d)

        # º.boxModel
        # º.browser
        # º.cssHooks
        # º.cssNumber
        # º.ready
        # º.speed
        # º.support

        # º.ajax()
        # º.ajaxPrefilter()
        # º.ajaxSetup()
        # º.ajaxTransport()
        # º.Callbacks()
        # º.contains()
        # º.data()
        # º.Deferred()
        # º.dequeue()
        # º.each()
        # º.error()
        # º.escapeSelector()
        # º.extend()
        # º.get()
        # º.getJSON()
        # º.getScript()
        # º.globalEval()
        # º.grep()
        # º.hasData()
        # º.holdReady()
        # º.htmlPrefilter()
        # º.inArray()
        # º.isArray()
        # º.isEmptyObject()
        # º.isFunction()
        # º.isNumeric()
        # º.isPlainObject()
        # º.isWindow()
        # º.isXMLDoc()
        # º.makeArray()
        # º.map()
        # º.merge()
        # º.noConflict()
        # º.noop()

        print(º.now())

        # º.param()
        # º.parseHTML()
        # º.parseJSON()
        # º.parseXML()
        # º.post()
        # º.proxy()
        # º.queue()
        # º.readyException()
        # º.removeData()
        # º.sub()
        print(º.trim("  some tst \n   TEST."))
        # º.type()
        # º.unique()
        # º.uniqueSort()
        # º.when()


if __name__ == '__main__':
    unittest.main()
