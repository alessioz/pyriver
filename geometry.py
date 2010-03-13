# -*- coding: utf-8 -*-

class Segment:
    """
    It defines the segment of a river cross-section
    with its own roughness.
    """
    def __init__(self, 
		yzcoordSegm=None,
		roughness=None):
	self.yzcoordSegm = yzcoordSegm
	self.roughness = roughness

class Section:
    """
    It defines attributes and methods for a river cross-section.
    It's possible to define sub-segments of the section,
    each one with a different roughness.
    Example of usage:
	
	coord = [[0,10],[0,0],[10,0],[20,0],[20,10]]
	sect = Section(0, coord)
	sect.addSegment(sect.yzcoord[0:2], 35)
	sect.addSegment(sect.yzcoord[2:], 40)
    """
    def __init__(self, xaxis=None,
		yzcoord=None, erodible=True,
		roughness=None, discontinuity=False):
	self.xaxis = xaxis
	self.yzcoord = yzcoord
	self.erodible = erodible
	self.roughness = roughness
	self.discontinuity = discontinuity
	self.segment = []

    def addSegment(self, yzcoordSegm=None,
		    roughness=None):
	segment = Segment(yzcoordSegm, roughness)
	self.segment.append(segment)