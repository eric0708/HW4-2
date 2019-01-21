def add_arguments(parser):
    '''
    Add your arguments here if needed. The TAs will run test.py to load
    your default arguments.

    For example:
        parser.add_argument('--batch_size', type=int, default=32, help='batch size for training')
        parser.add_argument('--learning_rate', type=float, default=0.01, help='learning rate for training')
    '''
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--learning_rate', type=float, default=0.0005)
    parser.add_argument('--num_episodes', type=int, default=30000)
    parser.add_argument('--episode_start', type=int, default=0)
    parser.add_argument('--max_num_steps', type=int, default=100000)
    parser.add_argument('--gamma', type=float, default=0.99)
    parser.add_argument('--save_dir', type=str, default='save/')
    parser.add_argument('--log_dir', type=str, default='logs/')
    parser.add_argument('--load_saver', type=int, default=0)
    parser.add_argument('--saver_steps', type=int, default=100000)
    parser.add_argument('--output_logs', type=str, default='output.csv')
    parser.add_argument('--hidden_dim', type=int, default=256)

    return parser
