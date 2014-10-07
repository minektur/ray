#!/bin/bash
#usage ./q1.sh file string

grep $2 $1| head -4 | tail -1
