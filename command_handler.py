import logging
from playbook_interactions import lock_label, edit_labels, mark_potential, mark_condition, clear_condition, create_character, get_labels, get_conditions, get_potential, get_pending_advancements, get_advancements
from config_interactions import get_settings, get_language, get_teamname, update_lang, update_gm, update_teamname, create_settings
from playbooks import get_moment_of_truth, get_playbooks
from language_handler import get_translation

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO) #set logging level to INFO, DEBUG if we want the full dump

def handle_help(message, _lang):
    log_line = message.guild.name + "|" + message.channel.name + "|" + message.author.name + "|" + message.content
    logger.info(log_line)
    help_file = open("help", "r")
    response = help_file.read()
    return response


plain_commands_dict = {
  "helphere": handle_help,
  "lock": lock_label,
  "editlabels": edit_labels,
  "potential": mark_potential,
  "markcondition": mark_condition,
  "clearcondition": clear_condition,
  "create": create_character,
  "settings": get_settings,
  "language": get_language,
  "teamname": get_teamname,
  "update_lang": update_lang,
  "update_gm": lambda msg, _lang: update_gm(msg),
  "update_teamname": lambda msg, _lang: update_teamname(msg),
  "create_settings": lambda msg, _lang: create_settings(msg),
  "labels": get_labels, 
  "conditions": get_conditions, 
  "get_potential": get_potential, 
  "pending_advancements": get_pending_advancements, 
  "advancements": get_advancements
}


embed_commands_dict = {
  "mot": get_moment_of_truth,
  "playbooks": lambda _msg, lang: get_playbooks(lang)
}

def plain_command_handler(message, lang):
    command = message.content.split(" ")[0][1:]
    handler = plain_commands_dict.get(get_translation(lang, f'plain_commands.{command}'), lambda _msg, _lang: '')

    return handler(message, lang)


def embed_command_handler(message, lang):
    command = message.content.split(" ")[0][1:]

    handler = embed_commands_dict.get(get_translation(lang, f'embed_commands.{command}'), lambda _msg, _lang: '')

    return handler(message, lang)
