# -*- mode: python -*-

#Forma de ejecucion en Windows: pyinstaller --onefile Begin.spec
#La opcion --debug anade un listado del procedimiento paso a paso.
#La opcion --console anade la consola adicional a la interfaz grafica.
block_cipher = None
nombre_completo = 'MOEA_Software_Linux'
ruta_completa = '/home/drakon/Documentos/Tesis/Software Product/Source Code'

a = Analysis(['Begin.py'],
             pathex=[ruta_completa],
             binaries=None,
             datas=None,
             hiddenimports=[
                            'Model.Community.Community',
                            'Model.ChromosomalRepresentation.BinaryRepresentation',
                            'Model.ChromosomalRepresentation.FloatPointRepresentation',
                            'Model.Fitness.ProportionalFitness',
                            'Model.Fitness.LinearRankingFitness',
                            'Model.Fitness.NonLinearRankingFitness',
                            'Model.Operator.Selection.ProbabilisticTournament',
                            'Model.Operator.Selection.Roulette',
                            'Model.Operator.Selection.StochasticUniversalSampling',
                            'Model.Operator.Crossover.NPointsCrossover',
                            'Model.Operator.Crossover.UniformCrossover',
                            'Model.Operator.Mutation.BinaryMutation',
                            'Model.Operator.Mutation.FloatPointMutation',
                            'Model.SharingFunction.GenotypicSimilarity.HammingDistance',
                            'Model.SharingFunction.PhenotypicSimilarity.EuclideanDistance',
                            'Model.MOEA.VEGA',
                            'Model.MOEA.NSGAII',
                            'Model.MOEA.SPEAII',
                            'Model.MOEA.MOGA'
                           ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas +=  [('View/Image/delete.gif', ruta_completa + '/View/Image/delete.gif', 'DATA')]
a.datas +=  [('View/Image/delete_mini.gif', ruta_completa + '/View/Image/delete_mini.gif', 'DATA')]
a.datas +=  [('View/Image/unam_shield.gif', ruta_completa + '/View/Image/unam_shield.gif', 'DATA')]
a.datas +=  [('View/Image/sciences_shield.gif', ruta_completa + '/View/Image/sciences_shield.gif', 'DATA')]

a.datas +=  [('View/Image/unam_shield.ico', ruta_completa + '/View/Image/unam_shield.ico', 'DATA')]
a.datas +=  [('View/Image/unam_shield.xbm', ruta_completa + '/View/Image/unam_shield.xbm', 'DATA')]

a.datas +=  [('Controller/XML/Features.xml', ruta_completa + '/Controller/XML/Features.xml', 'DATA')]  
a.datas +=  [('Controller/XML/MOPExamples.xml', ruta_completa + '/Controller/XML/MOPExamples.xml', 'DATA')]
a.datas +=  [('Controller/XML/PythonExpressions.xml', ruta_completa + '/Controller/XML/PythonExpressions.xml', 'DATA')]

pyz = PYZ(a.pure, 
          a.zipped_data,
          cipher=block_cipher
         )

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=nombre_completo,
          debug=True,
          strip=False,
          upx=False,
          console=True,
          icon=ruta_completa + '/View/Image/unam_shield.ico'
         )
