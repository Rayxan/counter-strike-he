from hltv_data import HLTVClient

hltv_client = HLTVClient()

# Basic commands
# print(hltv_client.get_ranking()[0])
# print(hltv_client.get_matches()[0])
# print(hltv_client.get_results()[0])

teams = [hltv_client.get_matches()[0]["date"], hltv_client.get_matches()[0]["team_1"], 'x' , hltv_client.get_matches()[0]["team_1"]]

for i in teams:
    print(i)
    

    

