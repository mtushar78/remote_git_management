configs = {
    '172.31.2.3':{'creds':['172.31.2.3',8822,'root','Qpay@Nbl2018'],
                  'commands':{'pull': 'cd / && ls'}},
    '172.31.2.36':{'creds':['172.31.2.36',8822,'root','quickpay2@dc'],
					'commands':{
						'pull': ['cd /var/ && ls'],
						'branch': ['cd /opt/ && ls'] 
					}},
    '172.31.2.35':{'creds':['172.31.2.35',22,'root','cDRtGV@2021'],
					'commands':{
						'pull': ['cd /opt && ls'],
						'branch': ['cd /opt/lampp/htdocs/remit/ && git branch']
						}		
					},
    "172.104.185.128":{"creds":["172.104.185.128", 22, "root","diit@321#"],
                       "commands":{
                           "pull":["cd /var/ && ls"],
                           "push": ["cd /var/ && python3 --version"]
                           }
                       }
    }

