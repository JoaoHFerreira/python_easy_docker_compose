FROM public.ecr.aws/lambda/python:3.9


WORKDIR /var/task

COPY requirements.txt .
RUN pip install -r requirements.txt


CMD ["main.lambda_handler"]