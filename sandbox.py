##############################################################################################
# Yelp Crawler
# 
# File: sandbox.py
# Desc: testing space
##############################################################################################

import city_crawler as cc

##############################################################################################
"""
TEST: Main operations: crawl, push to DB, print items

TO DO:
	1. Make logging module
	2. Catch and parse 'search_results' attribute from snippet JSON
	3. Implement duplicate checking before pushing to DB
"""
SF = cc.CityCrawler('San Francisco', 'CA')
SF.crawl_yelp()

##############################################################################################
	