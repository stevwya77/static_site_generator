import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_short(self):
        props = { "href": "https://www.google.com", "target": "_blank", }
        node = HTMLNode(None, None, None, props)
        test = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(HTMLNode.props_to_html(node), test)

    def test_props_to_html_long(self):
        props = {
            "id": "main-header-01",
            "class": "btn btn-primary active",
            "href": "https://www.example.com/dashboard",
            "src": "/assets/images/hero-banner.webp",
            "alt": "Portrait of a smiling software developer",
            "title": "Click to view more details",
            "style": "display: flex; margin-top: 20px; color: #333;",
            "lang": "en-US",
            "type": "password",
            "value": "qwerty12345",
            "target": "_blank",
            "placeholder": "Enter your email address...",
            "disabled": "disabled",
            "required": "required",
            "width": "1920",
            "height": "1080",
            "name": "user_submission_form",
            "rel": "noopener noreferrer",
            "method": "POST",
            "action": "/api/v1/submit",
            "autocomplete": "current-password",
            "data-id": "99db73-f12a-4c88",
            "loading": "lazy",
            "role": "navigation"
            }
        node = HTMLNode(None, None, None, props)
        test = ' id="main-header-01" class="btn btn-primary active" href="https://www.example.com/dashboard" src="/assets/images/hero-banner.webp" alt="Portrait of a smiling software developer" title="Click to view more details" style="display: flex; margin-top: 20px; color: #333;" lang="en-US" type="password" value="qwerty12345" target="_blank" placeholder="Enter your email address..." disabled="disabled" required="required" width="1920" height="1080" name="user_submission_form" rel="noopener noreferrer" method="POST" action="/api/v1/submit" autocomplete="current-password" data-id="99db73-f12a-4c88" loading="lazy" role="navigation"'
        self.assertEqual(HTMLNode.props_to_html(node), test)

    def test_props_to_html_empty(self):
        props = { }
        node = HTMLNode(None, None, None, props)
        test = ""
        self.assertEqual(HTMLNode.props_to_html(node), test)