from django.test import TestCase
from socialtags.templatetags.social_tags import fully_qualified
from django.template import Template, Context

class AlertTests(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def render(self, tag, url):
        t = Template('{%% load social_tags %%}{%% %s url %%}' % tag)
        return t.render(Context({'url': url})).strip()


    def test_twitter_share(self):
        twitter_res = """
<a href="http://twitter.com/share" class="twitter-share-button" data-url= "http://google.com" data-count="vertical">Tweet</a>
<script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>
        """.strip()
        
        rendered = self.render("twitter_share", "http://google.com")
        
        self.assertEqual(rendered, twitter_res)


    def test_facebook_share(self):
        facebook_res = """
<div id="fb-root"></div>
<script src="http://connect.facebook.net/en_US/all.js#xfbml=1"></script>
<fb:like href="http://google.com" send="true" width="450" show_faces="true" font=""></fb:like>
        """.strip()
        
        rendered = self.render("facebook_share", "http://google.com")
        
        self.assertEqual(rendered, facebook_res)
        
        
    def test_linkedin_share(self):
        linkedin_res = """
<script type="text/javascript" src="http://platform.linkedin.com/in.js"></script>
<script type="in/share" data-url="http://google.com" data-counter="top"></script>
        """.strip()
        
        rendered = self.render("linkedin_share", "http://google.com")
        
        self.assertEqual(rendered, linkedin_res)
        
        
    def test_email_share(self):
        email_res = """
<a href="mailto:?subject=I wanted you to see this site&amp;body=Check out this site http://google.com" title="Share by Email">Email</a>
        """.strip()
        
        rendered = self.render("email_share", "http://google.com")
        
        self.assertEqual(rendered, email_res)    


    def test_google_plus(self):
        google_res = """
<script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
<g:plusone href="http://google.com"></g:plusone>
        """.strip()
        
        rendered = self.render("google_plus", "http://google.com")
        
        self.assertEqual(rendered, google_res)

        
    def test_absolute_url(self):    
        self.assertEqual(fully_qualified("/"), "http://example.com/")
        self.assertEqual(fully_qualified("/profile/testuser"), "http://example.com/profile/testuser")
   
    
    def test_sans_http(self):
        self.assertEqual(fully_qualified("google.com"), "http://google.com")
        self.assertEqual(fully_qualified("google.com/analytics"), "http://google.com/analytics")
        self.assertEqual(fully_qualified("blob"), "http://blob")
    
    
    def test_full(self):
        self.assertEqual(fully_qualified("http://google.com"), "http://google.com")
        self.assertEqual(fully_qualified("http://google.com/?q=hello"), "http://google.com/?q=hello")
      
            
    def test_no_data_or_bad_data(self):
        self.assertEqual(fully_qualified(123), "")
        self.assertEqual(fully_qualified(None), "")
            