RUN_DEP = fastText/fasttext ./exceptions.py ./preprocessors/__init__.py ./preprocessors/featurematrixconversion.py ./preprocessors/mutualinformation.py ./preprocessors/featureselectionbase.py ./preprocessors/dumpfasttext.py ./preprocessors/chisquare.py ./preprocessors/preprocessingbase.py ./my_statistics.py ./classifiers/__init__.py ./classifiers/baseline.py ./classifiers/fasttext.py ./classifiers/classifierbase.py ./classifiers/naivebayes.py ./utils.py ./load_data.py ./process_data.py

DATA_GEN_DEP = ./denormalization/extract_ids.py ./denormalization/filter.py ./denormalization/join.py

EXPS = $(basename $(wildcard experiments/*yaml))
EXPS_SAM = $(addsuffix .samp,$(EXPS))

data/data.json data/ids: $(DATA_GEN_DEP)
	# run denormalize
	./denormalization/denormalize.sh ../data/dataset data/data.json data/ids

data/geneea.json: data/ids $(DATA_GEN_DEP)
	# run geenea
	echo 'Copy geneea.json data into `data/`, source ids are in `data/ids`'
	echo 'Continue with enter.'
	read

$(EXPS): data/data.json data/geneea.json $(RUN_DEP)
	mkdir -p graphs
	./process_data.py '$@.yaml' data/data.json data/geneea.json

run: $(EXPS)
run_sample: $(EXPS_SAM)

$(EXPS_SAM): data/data_sample.json data/geneea_sample.json $(RUN_DEP)
	mkdir -p graphs
	./process_data.py '$(basename $@).yaml' data/data_sample.json data/geneea_sample.json

clean:
	rm -f data/data_fasttext_model.{bin,vec} data/data_fasttext_train
	rm -r fastText

fastText/fasttext:
	wget https://github.com/facebookresearch/fastText/archive/v0.2.0.zip
	unzip v0.2.0.zip
	mv fastText-0.2.0 fastText
	cd fastText && make
	rm -f v0.2.0.zip

test:
	./run_unittests.sh

thesis.pdf:
	cd diplomky/en && make

all: run thesis.pdf

.DEFAULT: all
.PHONY: all run run_sample clean $(EXPS) $(EXPS_SAM)
