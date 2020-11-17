
$\max(b_i - c_i) \cdot Prob(b_i < \min B) \\ $
$B = \text{Conjunto de Lances das outras Firmas} \\ $
$b_i = \text{Lance} \\ $
$c_i = \text{Custo de Produção} \\ $
$b(c_i) = \text{Função que determina Lance Ótimo a partir do Custo de Produção } (b'(c_i) > 0) \\ $
$\max(b_i - c_i) \cdot Prob(b_i < \min B) \iff \max(b_i - c_i) \cdot Prob (b'(b_i) < \min C) \\ $
$Prob(b'(b_i) < \min C) = g(b^{-1}(b_i)) \\ $
$\max(b_i - c_i) \cdot g(b^{-1}(b_1)) \\ $
$\frac{\partial (b_i - c_1) \cdot g(b^{-1}(b_1))}{\partial b_i} = g(b^{-1}(b_i))+ (b_i - c_i) \cdot \frac{g'(b^{-1}(b_1))}{b'(b^{-1}(b_i))} = 0 \\ $
$b^{-1}(b_i) = c_i \\ $
$b_i = b(c_i) \\ $
$g(c_i) + (b(c_i) - c_i) \cdot \frac{g'(c_i)}{b'(c_i)} = 0 \\ $
$g(c_i) \cdot b'(c_i) + g'(c_i) \cdot b(c_i) = g'(c_i) \cdot c_i \\ $
$b'(c_i) + \frac{g'(c_i)}{g(c_i)} \cdot b(c_i) = \frac{g'(c_i)}{g(c_i)} \cdot c_i \text{ (EDO)}\\ $
$ \frac{\partial ({\rm e}^{\frac{\int g'(c_i)}{g(c_i)}} \cdot b(c_i))}{\partial c_i} = {\rm e}^{\frac{\int g'(c_i)}{g(c_i)}} \cdot \frac{g'(c_i) \cdot c_i}{g(c_i)} \\ $
$ {\rm e}^{ln(g(c_i))} \cdot b(c_i) = \frac{\int {\rm e}^{ln(g(c_i))} \cdot {g'(c_i) \cdot c_i}}{g(c_i)}\\ $
$b(c_i) \cdot g(c_i) = \int{g'(c_i) \cdot c_i} \\ $
$b(c_i) = \frac{1}{g(c_i)} \cdot (g(c_i) \cdot c_i - \int{g(c_i)}) \\ $
$b(c_i) = c_i - \frac{\int{g(c_i)}}{g(c_i)} \\ $






