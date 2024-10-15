FROM public.ecr.aws/lambda/python:3.9


WORKDIR /var/task

COPY requirements .
RUN pip install -r requirements


CMD ["main.lambda_handler"]