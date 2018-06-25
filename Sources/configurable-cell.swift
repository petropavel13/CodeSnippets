---
title: "ConfigurableCell extension implementation"
summary: "ConfigurableCell implementation within protocol extension."
completion-scope: TopLevel
---

extension <#CellName#>: ConfigurableCell {

    func configure(with viewModel: <#ViewModelType#>) {
        self.viewModel = viewModel

        <#configuration#>
    }
}