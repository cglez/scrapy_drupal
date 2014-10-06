# Script that generates a node export file with the nodes extracted
# by the bot. This file can be imported using the node_export module.

import json, time, datetime, base64, os.path

file = open("data.json")
db = json.load(file)

for node in db:
  # Define the entities in node_export format
  node['title'] = "".join(node['title']).strip()

  pubdate = "".join(node['pubdate'])
  tcreation = time.strptime(pubdate, "%d %b %Y")
  node['created'] = time.mktime(tcreation)
  node['changed'] = time.mktime(tcreation)

  body = "".join(node['body'])
  summary = "".join(node['summary']).strip()
  node['body'] = {'und': [{'value':body, 'summary':summary, 'format':'full_html'}]}

  node['author'] = {'und': node['author']}

  node['field_tags'] = node['tags']

  # we can also import base64 encoded files
  if node['picture_url']:
    filespath = "example.com/sites/default/files/"
    subpath = "pictures/"

    pic_basename = "".join(node['picture_url']).rsplit('/', 1)[1]
    if os.path.isfile(filespath + subpath + pic_basename):
      filepic = open(filespath + subpath1 + pic_basename, 'rb')
      pic64 = str(base64.b64encode(filepic.read()))
    else:
      pic64 = ""

    if node['figcaption']:
      pictitle = "".join(node['figcaption']).strip()
    else:
      pictitle = ""

    node['field_picture'] = {'und': [{
      'fid': None,
      'uid': '1',
      'filename': pic_basename,
      'uri': 'public://pictures/' + pic_basename,
      'filemime': 'image/jpeg',
      #"filesize": "",
      'status': '1',
      'timestamp': int(time.mktime(tcreation)),
      #"uuid": "",
      #"rdf_mapping": [],
      "alt": '',
      "title": pictitle,
      #"width": "",
      #"height": "",
      "node_export_file_data": pic64,
    }]}

  node['uid'] = '1'
  node['name'] = 'admin'
  #node['log'] = []

  node['status'] = '0'
  node['promote'] = '1'
  node['sticky'] = '0'
  node['comment'] = '2'

  node['type'] = 'basic_page'
  node['language'] = 'en'
  #node['translate'] = '0'

  #node['data'] = ''
  #node['rdf_mapping'] = {
    #"rdftype": ["sioc:Item","foaf:Document"],
    #"title": {"predicates": ["dc:title"]},
    #"created":{"predicates":["dc:date","dc:created"],"datatype":"xsd:dateTime","callback":"date_iso8601"},
    #"changed":{"predicates":["dc:modified"],"datatype":"xsd:dateTime","callback":"date_iso8601"},
    #"body":{"predicates":["content:encoded"]},
    #"uid":{"predicates":["sioc:has_creator"],"type":"rel"},
    #"name":{"predicates":["foaf:name"]},
    #"comment_count":{"predicates":["sioc:num_replies"],"datatype":"xsd:integer"},
    #"last_activity":{"predicates":["sioc:last_activity_date"],"datatype":"xsd:dateTime","callback":"date_iso8601"}
  #}

  node['node_export_drupal_version'] = '7'
  node['#node_export_object'] = '1'

print(json.dumps(db))
