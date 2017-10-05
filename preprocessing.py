import unicodecsv as csv
import json
import codecs
from io import BytesIO
f = BytesIO()
dict1 = {'1':"January","2":"February","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"September","10":"October","11":"November","12":"December"}
fieldnames = ['id','title','production_name','country_name','release_year','release_month','genre_name','budget','revenue','runtime','vote_average','vote_count']
f = codecs.open('processed_data.csv', 'a',"utf-8")
with open('tmdb_5000_movies.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    writer = csv.DictWriter(f,fieldnames=fieldnames,encoding='utf-8')
    writer.writeheader()
    count = 0
    count2 = 0
    for row in reader:
        a = str(unicode(row['production_companies']))
        s = json.loads(a)
        if isinstance(s,list):
            try:
                s2 = s[0]
            except:
                count2 += 1
                continue
            if isinstance(s2,dict):
                production_name = s2.get("name")


        b = str(unicode(row['genres']))
        s = json.loads(b)
        if isinstance(s,list):
            try:
                s2 = s[0]
            except IndexError:
                count2 += 1
                continue
            if isinstance(s2,dict):
                genre_name = s2.get("name")


        c = str(unicode(row['production_countries']))
        s = json.loads(c)
        if isinstance(s, list):
            try:
                s2 = s[0]
            except:
                count2 += 1
                continue
            if isinstance(s2, dict):
                country_name = s2.get("name")




        d = str(unicode(row['release_date']))
        s = d.split("/")

        release_year = s[2]
        release_month = dict1.get(s[0])

        try:
            dict2 = {'production_name':production_name,'genre_name':genre_name,'country_name':country_name,'release_year':release_year,'release_month':release_month,'revenue':str(unicode(row['revenue'])),'title':str(unicode(row['title'])),'runtime':str(unicode(row['runtime'])),'budget':str(unicode(row['budget'])),'vote_average':str(unicode(row['vote_average'])),'vote_count':str(unicode(row['vote_count'])),'id':str(unicode(row['id']))}

            writer.writerow(dict2)
        except UnicodeEncodeError:
            count2 += 1
            continue
        except UnicodeDecodeError:
            count2 += 1
            continue

        count += 1

print "Entries Preprocessed:",count
print "Entries Deleted:",count2





