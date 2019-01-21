Download the trained model from 

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