from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task
def process_file(file_id):
    """
    An asynchronous task to process a file.
    """
    from files.models import File
    entity = File.objects.get(id=file_id)

    try:
        # Log entry about the start of task execution
        logger.info(f'Starting processing file {file_id}')

        entity.processed = True
        entity.save()

        # Log entry about successful task completion
        return f'File id {entity.id} processed!'
    except Exception as e:
        # Log about an error when executing a task
        logger.error(f'Error processing file {file_id}: {str(e)}')
        raise