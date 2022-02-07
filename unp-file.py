import urllib.request

urlbase = 'https://s3-us-west-2.amazonaws.com/enterprises.unp.paso5/images/profile_'
for f in range(4950, 5011):
    urldef = urlbase + str(f) + '.PNG'
    print(urldef)
    #urllib.request.urlretrieve(urldef, localpath)