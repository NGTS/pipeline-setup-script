#!/usr/bin/env bash

set -e

# DATE: {{ date }}

BIAS_ACTIONS=({{ bias|add_spacings }})
DARK_ACTIONS=({{ dark|add_spacings }})
FLAT_ACTIONS=({{ flat|add_spacings }})
SCIENCE_ACTIONS=({{ science|add_spacings }})
PIPELINE_SHA="{{ pipeline_sha }}"

main() {
    source /ngts/pipedev/ParanalOutput/running-the-pipeline/init.sh
    setup_{{ planetname }}

    RUN_NAME={{ date|clean_date }}-{{ planetname }}
    ROOT_DIRECTORY=${BASEDIR}/${RUN_NAME}
    INITIAL_WCS_SOLUTION=$(python ./solution_mapping/query_for_solution.py --mysql --camera-id {{ camera_id }} --action ${SCIENCE_ACTIONS[0]})

    setup_actions_manually

    python ${AUX_DIR}/build-pipeline-directory.py -o ${ROOT_DIRECTORY} $(cat ${ACTIONLIST})
    cat $ACTIONLIST

    upload_start_job_status

    run_pipeline

    report_job_status
}

main
