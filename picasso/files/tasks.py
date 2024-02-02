from celery import shared_task
import mimetypes
import logging
import time

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

        # Processing files depending on type
        # example
        process_type_file(entity)

        # Log entry about successful task completion
        return f'File id {entity.id} processed!'
    except Exception as e:
        # Log about an error when executing a task
        logger.error(f'Error processing file {file_id}: {str(e)}')
        raise


def process_type_file(entity):
    """
    Example of a function to process 
    a file depending on its type
    """    
    file_type, _ = mimetypes.guess_type(entity.file.name)
    logger.info(f'File has type: {file_type}')

    # simulate a delay when processing a file
    time.sleep(60)

    # after the file type is determined
    # the necessary processing can occur
    entity.processed = True
    entity.save()