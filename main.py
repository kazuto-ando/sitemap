# -*- coding: utf-8 -*-


import urllib2
import csv


def xml_header():
    xml_header = """
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

"""[1:-1]
    f = open("sitemap.xml","a")
    f.write(xml_header)
    s = '\n'
    f.write(s)
    f.close()


def create_sitemap():
    reader = csv.reader(open('urls.csv', 'r'))
    url_list = []

    for row in reader:
       url_list = row

    for url in url_list:
        try:
            req = urllib2.urlopen(url)
            status_code= req.getcode()
            if (status_code == 200):
                sitemap =  """
<url>
    <loc>{url}</loc>
</url>
                """.format(url=url).strip()

                f = open("sitemap.xml","a")
                f.write(sitemap)
                s = '\n'
                f.write(s)
                f.close()

        except urllib2.HTTPError as e:
            print 'HTTPError'
        except urllib2.URLError as e:
            print 'URLError'


if __name__ == '__main__':
    xml_header();
    create_sitemap();
