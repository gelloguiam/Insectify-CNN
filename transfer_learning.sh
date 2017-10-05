rm -rf bottlenecks/
rm -rf output_graph/
rm -f *.pb
rm -f *.txt

./src/retrain_model.sh
./src/optimize_model.sh
