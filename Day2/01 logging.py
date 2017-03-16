import logging

def main():
    x = 10

    logging.basicConfig(filename='myapp.log',
                        level=logging.DEBUG,
                        format='%(levelname)s: %(asctime)s %(message)s',
                        datefmt='%Y/%m/%d %H:%M:%S ')
    logging.info("This is info from main")
    logging.error('Oh no. Got an error')
    logging.debug("Hmmm x = {}".format(x))


if __name__ == '__main__':
    main()