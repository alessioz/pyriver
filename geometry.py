# -*- coding: utf-8 -*-
class Section:
    def __init_(self, xaxis=None,
		yzcoordinates=None, erodible=True,
		roughness=None, discontinuity=False):
	self.xaxis = xaxis
	self.yzcoordinates= yzcoordinates
	self.erodible = erodible
	self.roughness = roughness
	self.discontinuity = discontinuity
	self.segments = []
