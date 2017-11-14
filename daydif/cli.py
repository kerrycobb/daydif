#!/usr/bin/env python3

import click
import daydif as dd

@click.command()
@click.argument('startdate')
@click.argument('enddate', required=False)

def cli(startdate, enddate):
	days = dd.daydif(startdate, enddate)
	print (days)

if __name__=='__main__':
    cli()
