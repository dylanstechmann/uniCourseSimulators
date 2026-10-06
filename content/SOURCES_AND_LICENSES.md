# Sources and licensing boundaries

uniStemCourseSimulators uses public university materials as curriculum comparators.
The initial registry imports **no external instructional text, question,
answer key, figure, video, dataset, or other asset**. Links and course titles
are references, not evidence that a uniStemCourseSimulators course has equivalent depth.

The machine-readable registry is [sources/registry.json](sources/registry.json).
It preserves the prototype's 22 MIT reference IDs and adds three Johns
Hopkins references plus three MIT reuse-policy references. The recorded access
date is 2026-10-05. All 22 linked MIT course landing pages and the canonical JHU
pages were opened on that date. An access date is not a claim that every asset
or every outbound link on a source page has been checked.

## License boundaries

| Material | License or project handling |
| --- | --- |
| Original software and implementation documentation | Existing [MIT License](../LICENSE); unchanged |
| New original uniStemCourseSimulators educational content | [CC BY 4.0](../LICENSE-CONTENT), unless specifically marked otherwise |
| Preserved prototype educational content previously distributed under MIT | Historical MIT permissions retained; additionally offered under CC BY 4.0 |
| Future approved adaptations of applicable OCW material | CC BY-NC-SA 4.0 with source, faculty author, asset, license, and modification attribution |
| All-rights-reserved or license-excluded source assets | No import, adaptation, or redistribution under this project's content policy |
| JHU public catalogue and AAP descriptions | Link-only curriculum references; no open reuse license established |
| Other third-party assets | Explicit asset-specific license and attribution required before import |
| Learner data and submitted work | Outside repository licensing; governed by the learner's rights and deployment policy |

The full original-content license is linked from [LICENSE-CONTENT](../LICENSE-CONTENT).
Retaining historical MIT grants avoids restricting rights already granted to
prototype recipients. A future contributor must not mark third-party content
as original merely because it has been edited or converted to Markdown.

## How to interpret the registry

`reuse_mode: link-only-comparator` means the current repository only links to
that source. `permissions` records the operations selected for this project:
linking is enabled, while quotation, adaptation, and redistribution are not
approved for these initial records. The flags do not exhaust the legal
permissions of the underlying source. `rights_notes` explains this distinction.

An empty `imported_assets` array means no asset has been imported by that
record. `checksum: null` means no reproducible source snapshot or checksum has
been captured; it is not evidence that source content is unchanged. A source
can be mapped to a course without being a reading assignment, a copied
resource, a reviewer, or a complete coverage comparison.

## MIT OpenCourseWare use

The current [MIT OCW terms](https://ocw.mit.edu/pages/privacy-and-terms-of-use/)
identify CC BY-NC-SA 4.0 for applicable material, with attribution, license
links, modification identification, noncommercial use, and ShareAlike
requirements. Their displayed revision date is 08/11/2026. No use of MIT names
or marks may imply endorsement; product branding is uniStemCourseSimulators.

Before any future adaptation, inspect the exact asset and its credit lines.
The [OCW attribution guidance](https://mitocw.zendesk.com/hc/en-us/articles/4414774195355-How-do-I-properly-cite-my-reuse-of-OCW-content)
calls for the faculty author, course title, term, institution/source, and
license. The [OCW third-party guidance](https://mitocw.zendesk.com/hc/en-us/articles/4414756181403-How-is-all-rights-reserved-content-different-from-the-rest-of-OCW-content)
explains that excluded, all-rights-reserved material does not receive OCW's
Creative Commons permissions. Carry forward special third-party credit where
reuse is permitted. A course-level license entry cannot clear every asset.

The current terms also contain AI-training provisions. The project does not
use source-registry inclusion as authorization to train a model or send source
material to a feedback provider. Review that use separately if proposed.

## Asset intake record

Every future external asset needs a registry entry or an `imported_assets`
record with its repository path, exact source URL, title, author/copyright
holder, license, access date, version or checksum where reproducible,
attribution text, modification description, and any restrictions. Record
whether it is a link, quotation, adaptation, or redistribution. Preserve
asset-specific notices in the rendered course as well as this registry.

No third-party asset is currently listed as imported. The existing favicon and
UI are repository software assets under MIT; no MIT or JHU logo is imported.
