from flask import Flask, request, jsonify
app = Flask(__name__)

voting_list = ['18BCE0269','18BCE0833','18BCE0834']
party_dict = {1:'BJP',2:'Congress',3:'Communist'}
vote_count = {'BJP':0,'Congress':0,'Communist':0}
voters_dict = {'18BCE0269':0,'18BCE0833':0,'18BCE0834':0}

@app.route('/vote',methods=['POST'])
def vote():
    voter_data = request.get_json()
    voter_id = voter_data['Voter ID']
    party_id = voter_data['Party']

    if voter_id not in voting_list:
        return "voting id doesn't exist,please try again"
    else:
        if voters_dict[voter_id] >= 1:
            return "same candidate"
        else:
            party_name = party_dict[party_id]
            vote_count[party_name] = vote_count[party_name]+1
            voters_dict[voter_id] = voters_dict[voter_id]+1
            return "vote is casted"

@app.route('/result',methods=["GET"])
def result():
    return jsonify(vote_count)

if __name__ == '__main__':
    app.run(debug=True)