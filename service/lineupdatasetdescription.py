import json
import tangelo

tangelo.paths('.')
from lineupdataset import translate


def run(displaymode):
    # Create an empty response object.
    response = {}

    if displaymode in ('left network only', 'right network only'):
        print 'displaying left or right'
        # return fixed result to compare two datasets
        response['primaryKey'] = 'entity'
        response['separator'] = '\t'
        response['url'] = 'service/lineupdataset'
        response['columns'] = [
            {'column': 'entity', 'type': 'string'},
            {'column': '1hop', 'type': 'number', 'domain': [0, 1]},
            {'column': '2hop', 'type': 'number', 'domain': [0, 1]}]
        response['layout'] = {'primary': [
            {'column': 'entity', 'width': 130},
            {'column': '1hop', 'width': 100},
            {'column': '2hop', 'width': 100},
            {'type': 'stacked', 'label': 'Combined', 'children': [
                {'column': '1hop', 'width': 75},
                {'column': '2hop', 'width': 75}]}]}
    else:
        # return fixed result to compare two datasets
        print 'displaying centered'
        response['primaryKey'] = 'entity'
        response['separator'] = '\t'
        response['url'] = 'service/lineupdataset'
        response['columns'] = [
            {'column': translate['entity'], 'type': 'string'},
            {'column': 'lsgm', 'type': 'number', 'domain': [0, 1]},
            {'column': translate['lev'], 'type':'number', 'domain': [0, 1]},
            {'column': translate['substring'], 'type':'number',
             'domain': [0, 1]},
            {'column': '1hop', 'type': 'number', 'domain': [0, 1]},
            {'column': '2hop', 'type': 'number', 'domain': [0, 1]}]
        response['layout'] = {
            'primary': [
                {'type': 'rank', 'width': 50},
                {'column': translate['entity'], 'width':100},
                {'type': 'stacked', 'label': 'Combined', 'children': [
                    {'column': 'lsgm', 'width': 150},
                    {'column': translate['lev'], 'width':120},
                    {'column': translate['substring'], 'width':120},
                    {'column': '1hop', 'width': 80},
                    {'column': '2hop', 'width': 80}]}]}

    # tangelo.log(str(response))
    return json.dumps(response)
