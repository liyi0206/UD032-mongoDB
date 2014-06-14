import requests

def main():
####    
    params={"query":"artist:Nirvana","fmt":"json"}
    r = requests.get("http://musicbrainz.org/ws/2/artist/", params=params)
    print "requesting", r.url
    
    if r.status_code == requests.codes.ok:
        results = r.json()
    else:
        r.raise_for_status()        
        
####
    artist_id = results["artist"][1]["id"]
    print artist_id
    
    params={"fmt":"json","inc": "releases"}
    r = requests.get("http://musicbrainz.org/ws/2/artist/"+artist_id, params=params)
    print "requesting", r.url
    
    if r.status_code == requests.codes.ok:
        artist_data = r.json()
    else:
        r.raise_for_status()
    
    releases = artist_data["releases"]
    release_titles = [r["title"] for r in releases]
    print "\nALL TITLES:"
    for t in release_titles:
        print t


if __name__ == '__main__':
    main()
