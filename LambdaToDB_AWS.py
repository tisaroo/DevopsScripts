def lambda_handler(event,context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key'])
    copy_source = {'Bucket':source_bucket , 'Key':key}
    print(event)
    
    #just print function
    print("Log stream name : ", context.log_stream_name)
    print("Log group name : ", context.log_group_name)
    print("Request Id:", context.aws_request_id)
    print("Mem. limit(MB): ", context.memory_limit_in_mb)
    
    try:
        print("Using waiter to waiting for object to persist thru s3 service")
        waiter = s3.get_waiter('object_exists')
        waiter.wait(Bucket=source_bucket, Key=key)
        print("Accessing the receied file and reading the same")
        bucket = tests3.Bucket(u'awslambdas3test2')
        obj = bucket.Object(key='inputfile.csv')
        response = obj.get()
        print("response from file object")
        print(response)
        lines = response['Body'].read().split()
        print(response['Body'].read())
        
        # creating a list of dictionaries from the csv file records
        recList = list()
        i = 0
        while i < len(lines):
            record  = {}
            record['username'] = lines[i]
            record['lastname'] = lines[i+1]
            print(record)
            recList.append(record)
            i = i+2
        print(recList)    
        insert_data(recList)
        
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, source_bucket))
        raise e