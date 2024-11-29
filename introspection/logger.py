import logging

logging.basicConfig(
    filename="introspection.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log_action(agent_id, action):
    logging.info(f"Agent {agent_id}: {action}")
