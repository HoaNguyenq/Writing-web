import os
import pickle


buzzwords = {'entitlement', 'javascript', 'client-centric', 'nanotechnology', 'profit center', 'eyeballs', 'differentiated instruction', 'water under the bridge', 'engine', 'amplify', 'paas', 'pain point', 'time-blindness', 'analytics', 'cloud-computing', 'information superhighway', 'digital literacy', 'benchmarking', 'instructional scaffolding', 'catchphrase', 'on the runway', 'mashup', 'frictionless', 'home', 'brick-and-mortar', 'buzzword compliant', 'psychobabble', 'robust', 'solidarity', 'tagging', 'wellness', 'deep dive', 'html5', 'reach out', 'growth hacking', 'single pane-of-glass', 'sustainability', 'microservices', 'rustic', 'open source', 'hyperlocal', 'webinar', 'business-to-business', 'alignment', 'one team', 'survival strategy', 'beta', 'core competency', 'folksonomy', 'holistic', 'design pattern', 'fit for purpose', 'drill down', 'management visibility', 'political capital', 'stack', 'headlights', 'accountable talk', 'framework', 'higher-order thinking', 'social software', 'invested in', 'agile', 'streamline', 'bleeding edge', 'passionate', 'deep learning', 'run like a business', 'roadmap', 'law of the instrument', 'millennial', 'enable', 'holistic approach', 'organic growth', 'mindshare', 'resonate', 'generation x', 'reimagine', 'eating your own dogfood', 'paralysis by analysis', 'take offline', 'innovation', 'dot-bomb', '4g', 'leverage', 'iaas', 'startup', 'bandwidth', 'coward', 'bio-', 'best practices', 'business process outsourcing', 'customer-centric', 'eco-', 'lateral violence', 'seamless', 'solution', 'memetics', 'front-end', 'bricks-and-clicks', 'fuzzy logic', 'work smarter', 'reverse fulfilment', 'value add', 'saas', 'offshoring', 'spin-up', 'ideation management', 'ambiguity', 'heavy lifting', 'clear goal', 'back-end', 'mission critical', 'unpack', 'social bookmarking', 'emotional intelligence', 'quick win', 'bring your own device', 'convergence', 'cross-platform', 'artisan', 'end-to-end', 'scalability', 'software defined networking', 'spam', 'visibility', 'power word', 'lambda', 'vortal', 'disruptive innovation', 'virtue word', 'enterprise service bus', 'transmedia', 'weasel word', 'flipped classroom', 'ajax', 'optics', 'project-based learning', 'break through the clutter', 'quantum supremacy', 'viral', 'systems development life-cycle', 'next generation', 'algorithm', 'herding cats', 'data science', 'establishment', 'return on investment', 'grow', 'mind share', 'virtualization', 'datafication', 'storytelling', 'big society', 'building capabilities', 'sea change', 'co-opetition', 'tiger team', 'mouthfeel', 'netiquette', 'bring to the table', 'close the loop', 'face time', 'immersion', 'generation y', 'long tail', 'new economy', 'spa', 'opportunities', 'empowerment', 'share options', 'buzzword', 'exit strategy', 'digital rights management', 'internet of things', 'pleonasm', 'cyber-physical systems', 'digital remastering', 'wheelhouse', 'andon', 'ballpark figure', 'push the envelope', 'think outside the box', 'real-time', 'corporate jargon', 'best of breed', 'digital signage', 'early-stage', 'rightshoring', 'sox', 'user generated content', 'content marketing', 'ephemeral rogue entity', 'talent relationship management', 'creative', 'free value', 'warfighter', 'multiple intelligences', 'web 2.0', 'moving forward', 'content management system', 'big data', 'web services', 'going forward', "bloom's taxonomy", 'machine learning', 'new normal', 'sisterhood', 'national security', 'devops', 'stakeholder', 'collaboration', 'business-to-consumer', 'evangelist', 'paradigm', 'e-learning', 'serum', 'synergy', 'come-to-jesus moment', 'digital divide', 'blockchain', 'knowledge process outsourcing', 'make it pop', 'bizmeth', 'privacy', 'touchpoint', 'toolchain', 'wikiality', 'hype cycle', 'value-added', 'clickthrough', 'document management', 'sensorization', 'css3', 'modularity', 'workflow', 'mobile', 'marketing buzz', 'event horizon', 'fulfilment issues', 'drinking the kool-aid', 'fleet dynamism', 'disruptive technologies', '5g', 'at the end of the day', 'employer branding', 'impact', 'logistics', 'globalization', 'paradigm shift', 'common core', 'skeuomorphic', 'innovative', 'api', 'strategic communication', 'podcasting', 'strategic ineptness', 'information society', 'data mining', 'cadence', 'guided reading', 'productivity', 'content management', 'student engagement', 'win-win', 'downsizing', 'low hanging fruit', 'proactive', 'diversity', 'responsive web design', 'enterprise content management', 'list of buzzwords', 'sync-up', 'deep web'}
# print(buzzwords)
# print(len(buzzwords)) = 274

buzzwords_path = '/Users/hoanguyen' + '/expresso_website/nlp_data/buzzwords.pickle'
# os.getenv('HOME')

if not os.path.isfile(buzzwords_path):
 with open(buzzwords_path, 'wb') as file:
  pickle.dump(buzzwords, file, pickle.HIGHEST_PROTOCOL)
  file.close()