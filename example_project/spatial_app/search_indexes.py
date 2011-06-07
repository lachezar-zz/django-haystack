from haystack.indexes import *
from haystack import site
from spatial_app.models import SpatialTest
import random

# More typical usage involves creating a subclassed `SearchIndex`. This will
# provide more control over how data is indexed, generally resulting in better
# search.
class SpatialTestIndex(SearchIndex):

	name = CharField(document=True, model_attr='name')
	position = LocationField()
    
	def get_queryset(self):
		return SpatialTest.objects
	
	def prepare_position(self, obj):
        # store as "lat,lon"
		return u'%f,%f' % (11.2,22.22)#((random.random()-0.5)*180, (random.random()-0.5)*360)

site.register(SpatialTest, SpatialTestIndex)

