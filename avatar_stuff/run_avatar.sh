#The purpose of this script is to format data (.csv) into the proper avatar format,
#create the necessary .name file, then build a tree, with options to create a .dot
#file representation of the tree(s), and test model accuracy using cross-validation


#Format data into an avatar .data file (utilizes python script)
#python ./format_data.py

#Create the necessary .name file 
#./bin/data_inspector -w -d ternary_iso.data -t 0

#Build avatar tree(s)
#./bin/avatardt --format='avatar' --test --filestem='ternary' --output-probabilities 

#Best recipe for ternary data
./bin/avatardt --format='avatar' --train --filestem='ternary_iso' --split-method=C45 --bagging --use-stopping-algorithm --boosting --random-subspaces=100

#Create .dot file to view trees
#./bin/tree2dot 'droptol_tree.trees' 

#Cross-validate tree(s) to test accuracy
#./bin/crossvalfc -o avatar --folds=10 -f ternary_iso --output-confusion-matrix --seed=24601 --split-method=C45 --no-save-trees --bagging --use-stopping-algorithm --boosting --random-subspaces=100 --output-probabilities
#--boosting --random-subspaces --output-probabilities 

#Test training tree with testing data for accuracy
#./bin/avatardt --test -o avatar -f ternary_droptols --exclude=1-3,6,12-15 --output-confusion-matrix

#python ./format_data.py

#for i in  0.05 0.075 0.1 0.025
#do
#./bin/data_inspector -w -d $i.data -t 0 
#./bin/avatardt --format='avatar' --train --filestem=0.05 --exclude=1-3,6,11-15 --split-method=C45 --seed=24601 --random-forests --bagging --use-stopping-algorithm
#./bin/tree2dot 0.025.trees 
#done

#./bin/crossvalfc -o avatar --folds=10 -f 0.05 --exclude=1-3,6,11-15 --seed=24601 --output-confusion-matrix --no-save-trees --no-rigorous-strat --split-method=C45 --random-forests --bagging --use-stopping-algorithm --output-probabilities

