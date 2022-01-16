import json
def formatjson(json_data):
    """
    Formats the JSON data to be more readable.
    """
    with open("sorted.json", "w") as f:
        json.dump(json_data, f, indent=4)
    # json.dumps(json_data, sort_keys=True, indent=4)

def reformatjson(filename):
    """
    Reformats the JSON data to be more readable.
    """
    with open(filename) as json_file:
        json_data = json.load(json_file)
        formatjson(json_data)
    
# d = reformatjson(r'C:\Users\nihal\Downloads\a_coco.json')

def splitjson(filename):
    with open(filename) as json_file:
        trainsize = 199

        json_data = json.load(json_file)

        train_data = {}
        test_data = {}
        # copy the info and categories to the train and test data
        train_data['info'] = json_data['info']
        test_data['info'] = json_data['info']
        train_data['categories'] = json_data['categories']
        test_data['categories'] = json_data['categories']
        # copy the images to the train and test data based on the size
        train_data['images'] = json_data['images'][:trainsize]
        test_data['images'] = json_data['images'][trainsize:]
        # copy the annotations to the train and test data based on the size
        train_data['annotations'] = json_data['annotations'][:trainsize]
        test_data['annotations'] = json_data['annotations'][trainsize:]
        # copy the licenses to the train and test data
        train_data['licenses'] = json_data['licenses']
        test_data['licenses'] = json_data['licenses']
        # write the train and test data to the files
        with open('train.json', 'w') as outfile:
            json.dump(train_data, outfile, indent=4)
        with open('val.json', 'w') as outfile:
            json.dump(test_data, outfile, indent=4)
        # with open('train.json', 'w') as f:

splitjson(r'C:\Users\nihal\Downloads\sorted.json')
