import peon
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
log.setLevel(logging.INFO)

bot = peon.Client()
bot.connect('localhost', 'peon', '', auth=False)

bot.player.enable_auto_action('eat')
bot.player.enable_auto_action('defend')
bot.player.enable_auto_action('gather')
bot.player.auto_gather_items.add('Wither Skeleton Skull')
bot.player.auto_gather_items.add('Bone')
bot.player.auto_hunt_settings = {'home': (-39, 64, -36), 'mob_types': ['Skeleton']}
bot.player.enable_auto_action('hunt')
