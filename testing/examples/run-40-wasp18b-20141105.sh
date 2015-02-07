#!/usr/bin/env bash

set -e

# DATE: 2014/11/05

BIAS_ACTIONS=(101141)
DARK_ACTIONS=(101143)
FLAT_ACTIONS=(101126)
SCIENCE_ACTIONS=(101140)
PIPELINE_SHA="59aa1ec756657430048c45beea8093ed724f5ea2"

main() {
    source /ngts/pipedev/ParanalOutput/running-the-pipeline/init.sh
    setup_wasp18b

    RUN_NAME=20141105-wasp18b
    ROOT_DIRECTORY=${BASEDIR}/${RUN_NAME}
    INITIAL_WCS_SOLUTION=$(python ./solution_mapping/query_for_solution.py --mysql --camera-id 804 --action ${SCIENCE_ACTIONS[0]})

    setup_actions_manually

    python ${AUX_DIR}/build-pipeline-directory.py -o ${ROOT_DIRECTORY} $(cat ${ACTIONLIST})
    cat $ACTIONLIST

    upload_start_job_status

    run_pipeline

    report_job_status
}

main
