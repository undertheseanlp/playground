import checklist
from checklist.editor import Editor
import numpy as np

editor = Editor(language='vietnamese')
ret = editor.template('{vi_first_name} là một {profession} ở {vi_country}.',
                      vi_first_name=['Long', 'Hạnh', 'Tâm'],
                      profession=['bác sỹ', 'thầy giáo'],
                      vi_country=['Hà Nội'])
print(np.random.choice(ret.data, 3))
