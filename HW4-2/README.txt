Download the trained model from https://drive.google.com/file/d/1Xcul_39ihoQ8qA_jg-A39DeLiUgFMgkr/view?fbclid=IwAR3TrBohibjPG-JSNVvUMqLVuZOYpRen1yAQ_N-1Cqx4695r_gHe0-kJ7zY

Update the "argument.py" and "agent_dir/agent_dqn.py" in your hw4 file.
Put the save file in your hw4 file.

To train DQN model:
   python3 main.py --train_dqn

To
test DQN model:

   python3 test.py --test_dqn

Default is dueling DQN.
To switch to vanilla DQN:
   In "argument.py", change '--dueling_dqn' to 0
