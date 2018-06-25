---
title: "Binder"
summary: "RxSwift Binder declaration inside class scope."
completion-scope: ClassImplementation
---

var <#name#>Binder: Binder<<#type#>> {
    return Binder(self) { base, value in
        <#code#>
    }
}