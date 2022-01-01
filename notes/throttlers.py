from rest_framework.throttling import UserRateThrottle


class GetRateThrottle(UserRateThrottle):
	scope = 'get'
	rate = '1000/day'


class PostRateThrottle(UserRateThrottle):
	scope = 'post'
	rate = '50/day'
