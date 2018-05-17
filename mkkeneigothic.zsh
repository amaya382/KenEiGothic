#!/bin/zsh

mkdir -p KenEiGothic
for X in N P; do
  ZIP="GenEiGothic${X}-1.1.zip"
  ZIP_PATH="GenEiGothic/${ZIP}"
  [ -f ${ZIP_PATH} ] \
    || wget https://okoneya.jp/font/${ZIP} -P GenEiGothic
  unzip -n ${ZIP_PATH} -d GenEiGothic
  NEW_DIR=KenEiGothic/KenEiGothic${X}; \
  mkdir -p ${NEW_DIR}
  find GenEiGothic/GenEiGothic${X} \
    -name '*.otf' \
    -exec zsh -c "\
      ORIG_PATH={}; \
      TMP=\$(basename \${ORIG_PATH%.otf}).ttf; \
      NEW=K\${TMP#G}; \
      NEW_PATH=${NEW_DIR}/\${NEW}; \
      WEIGHT=\${\${NEW#KenEiGothic?-}%.ttf}; \
      otfccdump \${ORIG_PATH} \
        | otfcc-c2q \
        | otfccbuild -o \${NEW_PATH}; \
      fontforge -lang=py -script mod_info.py \
        KenEiGothic 剣暎ゴシック ${X} \${WEIGHT} ${NEW_DIR}" \;
done

