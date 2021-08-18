from searchtweets import load_credentials, gen_request_parameters, collect_results, ResultStream

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    search_args = load_credentials(filename="twitter_keys.yaml",
                                   yaml_key="search_tweets_v2",
                                   env_overwrite=False)
    query = gen_request_parameters("snow lang:en is:retweet", None, results_per_call=100)
    print(query)
    tweets = collect_results(query,
                             max_tweets=100,
                             result_stream_args=search_args)

    for tweet in tweets[0:10]:
        for result in tweet["data"]:
            text = result["text"]
            print(text, end='\n\n')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
