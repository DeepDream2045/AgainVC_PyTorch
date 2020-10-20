import logging
from agent.trainer import Trainer
from util.parser import get_parser
from util.config import Config
from util.mytorch import same_seeds



logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(asctime)s | %(filename)s | %(message)s',\
     datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

def get_args():
    parser = get_parser(description='Train')
    
    # config
    parser.add_argument('--config', '-c', default='./config/train_again-c4s.yaml')

    # dryrun
    parser.add_argument('--dry', action='store_true', help='whether to dry run')

    # debugging mode
    parser.add_argument('--debug', action='store_true', help='debugging mode')

    # seed
    parser.add_argument('--seed', type=int, help='random seed', default=961998)

    parser.add_argument('--load', '-l', type=str, help='', default='')
    parser.add_argument('--njobs', '-p', type=int, help='', default=4)
    parser.add_argument('--total-steps', type=int, help='', default=100000)
    parser.add_argument('--verbose-steps', type=int, help='', default=10)
    parser.add_argument('--log-steps', type=int, help='', default=500)
    parser.add_argument('--save-steps', type=int, help='', default=5000)
    parser.add_argument('--eval-steps', type=int, help='', default=5000)

    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    config = Config(args.config)
    same_seeds(args.seed)

    trainer = Trainer(config=config, args=args)
    trainer.train(total_steps=args.total_steps,
        verbose_steps=args.verbose_steps,
        log_steps=args.log_steps,
        save_steps=args.save_steps,
        eval_steps=args.eval_steps)
    
