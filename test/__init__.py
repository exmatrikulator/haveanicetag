import unittest
import webapp.util
from webapp import app, db
from webapp.models import *
from webapp.util import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tagstest.db'

## class for all test cases
class TestUtilMethods(unittest.TestCase):

    ## setup the database
    def setUp(self):
        db.drop_all()
        db.create_all()
        db.session.add( Tag( name="green" ) )
        db.session.add( Tag( name="red" ) )
        db.session.add( Tag( name="blue" ) )
        db.session.add( Tag( name="yellow" ) )
        db.session.add( Tag( name="white" ) )
        db.session.add( Data( tags=get_tagList(["green","red"]), value = "test") )
        db.session.add( Data( tags=get_tagList(["red","blue"]), value = "test") )
        db.session.add( Data( tags=get_tagList(["blue","yellow", "red"]), value = "test") )
        db.session.add( Data( tags=get_tagList(["white"]), value = "test") )
        db.session.commit()

    ## test function for get_tag_object()
    # @test get_tag_object()
    def test_get_tag_object(self):
        self.assertNotEqual(get_tag_object("green"), None)
        self.assertEqual(get_tag_object("greens"), None)

    ## test function for get_tagList_like()
    # @test get_tagList_like()
    # def test_get_tagList_like(self):
    #     print(type(get_tagList_like("g")[0]))
    #     self.assertEqual( get_tagList_like("g") , list('1'))
    #     self.assertEqual( get_tagList_like("r")[0], "2")


    def test_get_tagList_by_search(self):
        self.assertEqual( get_tagList_by_search("b"), ["blue"])
        self.assertEqual( get_tagList_by_search("bl"), ["blue"])
        self.assertEqual( get_tagList_by_search("blue"), ["blue"])
        self.assertEqual( get_tagList_by_search("blues"), [])
        self.assertEqual( get_tagList_by_search("e"), ["blue", "green", "red", "white", "yellow"])
        self.assertEqual( get_tagList_by_search("l"), ["blue","yellow"])
        self.assertEqual( get_tagList_by_search("b'\""), ["blue"])

    def test_get_tagList_by_tags(self):
        self.assertEqual( get_tagList_by_tags(["green"]), ["red"])
        self.assertEqual( get_tagList_by_tags(["red"]), ["blue","green","yellow"])
        self.assertEqual( get_tagList_by_tags(["red","blue"]), ["yellow"])
        self.assertEqual( get_tagList_by_tags(["white"]), [])  #exists
        self.assertEqual( get_tagList_by_tags(["nakka"]), [])  #doesn't exsists
        self.assertEqual( get_tagList_by_tags([]), ["blue", "green", "red", "white", "yellow"])
        self.assertEqual( get_tagList_by_tags(["green'\""]), ["red"])

    def test_get_tagList_from_tags_by_search(self):
        self.assertEqual( get_tagList_from_tags_by_search(["red"], "g"), ["green"])
        self.assertEqual( get_tagList_from_tags_by_search(["red"], "e"), ["blue", "green", "yellow"])
        self.assertEqual( get_tagList_from_tags_by_search(["red","blue"], "e"), ["yellow"])
        self.assertEqual( get_tagList_from_tags_by_search(["red","blue"], "ed  "), [])
        self.assertEqual( get_tagList_from_tags_by_search(["red'\""], "g'\""), ["green"])

    def test_exist(self):
        self.assertTrue( exist(["red"]))
        self.assertTrue( exist(["red",]))
        self.assertTrue( exist(["red",""]))
        self.assertFalse( exist(["nakka"]))
        self.assertTrue( exist(["red","blue"]))
        self.assertFalse( exist(["nakka","red"]))
        self.assertTrue( exist([]))
        self.assertTrue( exist(["red'\""]))


    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
