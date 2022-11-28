import requests
import time 

def similarity_run(Daily_memory, Starting_index):
    real_start = time.time()
    output_list = [""]
    for i in range(len(Daily_memory)-1-Starting_index):
        API_URL = "https://aefkgk2ttatnth29.us-east-1.aws.endpoints.huggingface.cloud"
        headers = {"Authorization": "Bearer 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"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        sentence = []
        for b in range(len(Daily_memory)-2):
            b+=1
            sentence.append(Daily_memory[b].text)
        


        
        start_time = time.time()
        output = query({
            "inputs": {
                "source_sentence": (Daily_memory[i+Starting_index]).text,
                "sentences": [
                    *((c) for c in sentence)
                ]
            },
        })



        print(" time taken: " + str(round((time.time() - start_time), 3)) + " seconds")
        output_list.append(output)
    print("Total time: " + str(round((time.time() - real_start),3)) + " seconds")
    return output_list
def layered_run(layer_list):
    API_URL = "https://aefkgk2ttatnth29.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {"Authorization": "Bearer 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"}
    def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
    start_time = time.time()
    layer_output_list = []
    for i in range(len(layer_list)):
            sentence = layer_list
            output = query({
            "inputs": {
                "source_sentence": layer_list[i],
                "sentences": [
                    *((b) for b in sentence)
                ]
            },
        })
            layer_output_list.append(output)


    print("Total time: " + str(round((time.time() - start_time),3)) + " seconds")
    return layer_output_list

        

