#!/bin/sh

SRC_IMAGE_DIR=source/features/images
DEST_IMAGE_NORMAL_DIR=build/html/images
DEST_IMAGE_SMALL_DIR=build/html/images_small

# create directory if it does not exists:
if [ ! -d $DEST_IMAGE_SMALL_DIR ]; then
  echo creating directory: $DEST_IMAGE_SMALL_DIR
  mkdir -p $DEST_IMAGE_SMALL_DIR || exit
fi

if [ ! -d $DEST_IMAGE_NORMAL_DIR ]; then
  echo creating directory: $DEST_IMAGE_NORMAL_DIR
  mkdir -p $DEST_IMAGE_NORMAL_DIR || exit
fi

for f in ${SRC_IMAGE_DIR}/*.png; do
  baseimage=$(basename $f)
  echo converting image $f in ${DEST_IMAGE_SMALL_DIR}/${baseimage}
  convert -geometry 350x350 $f ${DEST_IMAGE_SMALL_DIR}/${baseimage} || exit
  echo copying image $f in ${DEST_IMAGE_NORMAL_DIR}
  cp $f $DEST_IMAGE_NORMAL_DIR || exit
done;

