export CLASSPATH=".:/usr/local/lib/antlr-4.8-complete.jar:$CLASSPATH"
java -jar /usr/local/lib/antlr-4.8-complete.jar LaTeX.g4 -no-visitor -no-listener -o _antlr
python3 rename.py
cd ../../../
python3 setup.py install
