from rest_framework.throttling import UserRateThrottle


class GetRateThrottle(UserRateThrottle):
	scope = 'get'
	rate = '5/day'


class PostRateThrottle(UserRateThrottle):
	scope = 'post'
	rate = '1/day'
