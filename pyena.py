# -*- coding: utf-8 -*-
from __future__ import division


class Reach:
	'''
	Utility for fluvial engineering.
	'''
	def __init__(self):
		self.g = 9.81
		self.delta = 1.65 # relative density of sediments respect to water
		self.theta_cr = 0.047
		
	def get_ks(self, d, ks_type='d50'):
		'''
		Compute Strickler roughness coefficient
		Ks [m^(1/3)s^-1]
		Also Manning coefficient is computed as attribute n
		
		Arguments:
		d: the d50 (or d90) diameter [m]
		ks_type: ks_type=d90 for Meyer-Peter Müller equation
		
		Example of usage:
			reach = Reach()
			reach.get_ks(0.05)
			reach.n #manning
		'''
		self.ks_type = ks_type
		self.d = d
		if self.ks_type == 'd50':	# Strickler			
			self.ks = 21.1/(self.d**(1/6))
		if self.ks_type == 'd90':	# Meyer-Peter Muller
			self.ks = 26/(self.d**(1/6))
		self.n = 1/self.ks	# Manning		
		return self.ks
	
	def get_theta(self, i, h, d):
		'''
		Compute Shields parameter 'theta'
		'''
		self.i,self.h, self.d = i, h, d
		
		self.u_star = (self.g*i*h)**0.5
		self.theta = self.u_star**2 /(self.g*self.delta*self.d)
		return self.theta

	def get_h(self, q, i,  B=1):
		'''
		Compute water level [m]
		'''
		self.i = i
		self.q = q
		self.B = B
		self.h = (self.q/(self.ks*(self.i**0.5)))**(3/5)
		if self.B != 1:
			diff = 10
			while diff > 0.1:
				self.h = self.h-0.001
				self.area = self.B*self.h
				self.perimeter = self.B+2*self.h
				q_iter=(self.area**(5/2))/(self.perimeter**(2/3))*self.ks*self.i**0.5
				diff = abs(self.q-q_iter)
			self.Rh = self.area / self.perimeter
		return self.h
	
	def get_qs(self, theta, theta_cr):
		'''
		Compute solid discharge
		'''
		self.theta = theta
		self.theta_cr = theta_cr
		self.qs = 8*(self.theta-self.theta_cr)**1.5 * (self.d * (self.g*self.delta*self.d)**0.5)
		return self.qs
	
	def get_i_theta(self, theta_cr, h, qs_proj):
		'''
		Compute project's slope
		'''
		self.theta_cr = theta_cr
		self.h = h
		self.qs_proj = qs_proj
		self.i_theta = self.theta_cr*(self.delta*self.d/self.h) \
		 + 0.25*(self.delta/self.h) * (self.qs_proj/((self.g*self.delta)**0.5))**(2/3)
		return self.i_theta


#example
q = 10.0 #discharge for unit of width [m^2/s]
d = 0.05 #diameter of the sediments
i = 0.02 #slope
g = 9.81 # yes, we are on earth

reach = Reach()
print 'ks', reach.get_ks(d)
print 'h prima', reach.get_h(q, i)
print 'theta', reach.get_theta(i, reach.h, reach.theta_cr)
print 'u star', reach.u_star
print 'qs', reach.get_qs(reach.theta, reach.theta_cr)
print 'i theta', reach.get_i_theta(reach.theta_cr, reach.h, reach.qs/2)